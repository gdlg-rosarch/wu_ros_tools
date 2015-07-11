Name:           ros-hydro-kalman-filter
Version:        0.2.4
Release:        0%{?dist}
Summary:        ROS kalman_filter package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kalman_filter
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-rospy
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-rospy

%description
Simple Kalman Filter in Python

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sat Jul 11 2015 David V. Lu!! <davidvlu@gmail.com> - 0.2.4-0
- Autogenerated by Bloom

* Thu Sep 04 2014 David V. Lu!! <davidvlu@gmail.com> - 0.2.3-1
- Autogenerated by Bloom

* Thu Sep 04 2014 David V. Lu!! <davidvlu@gmail.com> - 0.2.3-0
- Autogenerated by Bloom

* Mon Aug 18 2014 David V. Lu!! <davidvlu@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

