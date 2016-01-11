Name:           ros-indigo-costmap-converter
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS costmap_converter package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/costmap_converter
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-costmap-2d
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-costmap-2d
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs

%description
A ros package that includes plugins and nodes to convert occupied costmap2d
cells to primitive types.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jan 11 2016 Christoph Rösmann <christoph.roesmann@tu-dortmund.de> - 0.0.4-0
- Autogenerated by Bloom

* Wed Dec 23 2015 Christoph Rösmann <christoph.roesmann@tu-dortmund.de> - 0.0.3-0
- Autogenerated by Bloom

* Tue Dec 22 2015 Christoph Rösmann <christoph.roesmann@tu-dortmund.de> - 0.0.2-0
- Autogenerated by Bloom

* Mon Dec 21 2015 Christoph Rösmann <christoph.roesmann@tu-dortmund.de> - 0.0.1-0
- Autogenerated by Bloom

