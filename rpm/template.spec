Name:           ros-hydro-easy-markers
Version:        0.2.2
Release:        0%{?dist}
Summary:        ROS easy_markers package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/easy_markers
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-interactive-markers
Requires:       ros-hydro-roslib
Requires:       ros-hydro-rospy
Requires:       ros-hydro-tf
Requires:       ros-hydro-visualization-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-interactive-markers
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-visualization-msgs

%description
Python library to assist in publishing markers easily

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Aug 18 2014 David V. Lu!! <davidvlu@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

